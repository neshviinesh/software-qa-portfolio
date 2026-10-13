// File: src/pages/appointmentMath.test.js
import { describe, it, expect } from 'vitest';
import { formatTime, generateTimeSlots } from './appointmentMath';

describe('Temporal Formatting Utility (formatTime)', () => {
  it('should convert standard afternoon 24-hour time to 12-hour PM', () => {
    expect(formatTime('13:30')).toBe('1:30 PM');
  });

  it('should handle midnight (00:00) correctly', () => {
    expect(formatTime('00:00')).toBe('12:00 AM');
  });

  it('should handle noon (12:00) correctly', () => {
    expect(formatTime('12:00')).toBe('12:00 PM');
  });

  it('should handle early morning (07:00) correctly', () => {
    expect(formatTime('07:00')).toBe('7:00 AM');
  });

  it('should handle late evening (23:59) correctly', () => {
    expect(formatTime('23:59')).toBe('11:59 PM');
  });
});

describe('Slot Computation Algorithm (generateTimeSlots)', () => {
  const mockAvailability = {
    start_time: '09:00:00',
    end_time: '11:00:00',
    slot_duration_minutes: 30
  };

  it('should generate correct 30-minute slots', () => {
    // Faking a future date so past-time validation doesn't block it
    const slots = generateTimeSlots(mockAvailability, [], '2099-01-01');
    expect(slots).toEqual(['09:00', '09:30', '10:00', '10:30']);
  });

  it('should generate correct 60-minute slots', () => {
    const availability60 = { ...mockAvailability, slot_duration_minutes: 60 };
    const slots = generateTimeSlots(availability60, [], '2099-01-01');
    expect(slots).toEqual(['09:00', '10:00']);
  });

  it('should filter out slots that are already booked', () => {
    const bookedSlots = ['09:30', '10:30'];
    const slots = generateTimeSlots(mockAvailability, bookedSlots, '2099-01-01');
    expect(slots).toEqual(['09:00', '10:00']); 
  });

  it('should return an empty array if missing availability data', () => {
    const slots = generateTimeSlots(null, [], '2099-01-01');
    expect(slots).toEqual([]);
  });
});
