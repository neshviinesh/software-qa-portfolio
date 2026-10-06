import time
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from config import Config
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_webrtc_video_consultation_flow(dual_driver):
    """
    End-to-End Multiplayer Test:
    Navigates both Doctor and Patient through the Lobby into a live WebRTC Consultation.
    """
    doctor = dual_driver["doctor"]
    patient = dual_driver["patient"]

    # phase 1 : doctor has to initiate the consultation and call b4 patient can join
    doc_login = LoginPage(doctor)
    doc_login.load()
    doc_login.login(Config.DOCTOR_EMAIL, Config.DOCTOR_PASSWORD)
    doc_login.accept_consent_popup()

    # 1. navigate to the appt pages
    doctor.find_element(By.CSS_SELECTOR, "a.pd-nav-item[href*='/appointments']").click()

    # 2. clicking the correct appt card
    # wait up to 10 seconds for react to render the specific card
    target_card = "//div[contains(@class, 'pd-appt-meta') and contains(., 'Jun 16') and contains(., '12:00 PM') and contains(., 'Online')]"


    card_element = WebDriverWait(doctor, 10).until(EC.element_to_be_clickable((By.XPATH, target_card)))
    doctor.execute_script("arguments[0].click();", card_element)

    # 3. enter lobby
    lobby_btn = WebDriverWait(doctor, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'tele-btn') and contains(., 'Enter Lobby')]")))
    doctor.execute_script("arguments[0].click();", lobby_btn)

    # 4.  enter the call room
    call_room_btn = WebDriverWait(doctor, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'tele-btn-alt') and contains(., 'Enter Call Room')]")))
    doctor.execute_script("arguments[0].click();", call_room_btn)

    # 5. start the consultation : doctor's side
    start_call_btn = WebDriverWait(doctor, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'pd-btn-success') and contains(., 'Start Call')]")))
    doctor.execute_script("arguments[0].click();", start_call_btn)

    # Wait for the doctor's local video to render (fake media stream)
    time.sleep(2)
    doctor.find_element(By.TAG_NAME, "video")

    # phase 2 : patient logins, enter call room and join the call with doctor
    pat_login = LoginPage(patient)
    pat_login.load()
    pat_login.login(Config.PATIENT_EMAIL, Config.PATIENT_PASSWORD)
    pat_login.accept_consent_popup()

    # 1. navigate to the appt
    patient.find_element(By.CSS_SELECTOR, "a.pd-nav-item[href*='/appointments']").click()

    # 2. click the correct appt card
    target_card = "//button[contains(@class, 'pd-appt-row') and contains(., '16') and contains(., 'Jun') and contains(., '12:00 PM') and contains(., 'Online')]"
    patient_card = WebDriverWait(patient, 10).until(EC.element_to_be_clickable((By.XPATH, target_card)))
    patient.execute_script("arguments[0].click();", patient_card)

    # 3. enter the waiting room
    waiting_room_btn = WebDriverWait(patient, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'tele-btn') and contains(., 'Enter Waiting Room')]")))
    patient.execute_script("arguments[0].click();", waiting_room_btn)

    # 4. enter the call room
    pat_call_room_btn = WebDriverWait(patient, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'tele-btn-alt') and contains(., 'Enter Call Room')]")))
    patient.execute_script("arguments[0].click();", pat_call_room_btn)

    # 5. join the consultation call
    join_call_btn = WebDriverWait(patient, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'pd-btn-success') and contains(., 'Join Call')]")))
    patient.execute_script("arguments[0].click();", join_call_btn)

    # phase 3 : validate the webrtc handshake
    # Wait 5 seconds for Cloudflare TURN servers to negotiate the P2P connection
    time.sleep(5)

    # Check if the patient browser is actively receiving video frames from doctor
    patient_videos = patient.find_elements(By.TAG_NAME, "video")
    video_playing = False

    for video in patient_videos:
        # readyState 4  proves frames are streaming
        ready_state = patient.execute_script("return arguments[0].readyState;", video)
        if ready_state == 4:
            video_playing = True
            break

    assert video_playing == True, "WebRTC signaling failed or remote video frames are not rendering!"

    # watch connection visually
    time.sleep(3)

    # phase 4 : teardown
    # doctor ends the call
    doctor.find_element(By.XPATH, "//button[contains(@class, 'pd-btn-danger-ghost') and contains(., 'Leave Call')]").click()