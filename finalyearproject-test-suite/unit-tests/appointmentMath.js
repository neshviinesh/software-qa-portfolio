// File: src/pages/appointmentMath.js

export function formatTime(time24) {
  const [hourStr, minute] = time24.split(":");
  let hour = parseInt(hourStr, 10);
  const ampm = hour >= 12 ? "PM" : "AM";
  hour = hour % 12 || 12;
  return `${hour}:${minute} ${ampm}`;
}

export function generateTimeSlots(availability, bookedSlots, selectedDate, now = new Date()) {
  if (!availability?.start_time || !availability?.end_time || !selectedDate) return [];

  const slots = [];
  const duration = availability.slot_duration_minutes || 30;

  const [startHour, startMinute] = availability.start_time.slice(0, 5).split(":").map(Number);
  const [endHour, endMinute] = availability.end_time.slice(0, 5).split(":").map(Number);

  const start = new Date(`${selectedDate}T00:00:00`);
  start.setHours(startHour, startMinute, 0, 0);

  const end = new Date(`${selectedDate}T00:00:00`);
  end.setHours(endHour, endMinute, 0, 0);

  const current = new Date(start);
  const isToday = selectedDate === now.toISOString().split("T")[0];

  while (current < end) {
    const hh = String(current.getHours()).padStart(2, "0");
    const mm = String(current.getMinutes()).padStart(2, "0");
    const timeStr = `${hh}:${mm}`;
    const isPastToday = isToday && current <= now;
    
    if (!bookedSlots.includes(timeStr) && !isPastToday) {
      slots.push(timeStr);
    }
    current.setMinutes(current.getMinutes() + duration);
  }

  return slots;
}
