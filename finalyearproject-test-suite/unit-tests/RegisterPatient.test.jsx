import { describe, it, expect } from 'vitest';
import { validateIC, normalizeMYPhone } from './RegisterPatient'; // Adjust path if needed

describe('IC Validation (validateIC)', () => {
  it('accepts a valid Malaysian IC', () => {
    expect(validateIC('980123-10-5678')).toBeNull();
    expect(validateIC('010228-14-1234')).toBeNull(); // Valid leap year date
  });

  it('rejects ICs with missing hyphens or wrong length', () => {
    expect(validateIC('980123105678')).toContain('format');
    expect(validateIC('980123-10-567')).toContain('format'); // Too short
  });

  it('rejects invalid months', () => {
    expect(validateIC('981323-10-5678')).toContain('month'); // Month 13
    expect(validateIC('980023-10-5678')).toContain('month'); // Month 00
  });

  it('rejects invalid days for 30-day months', () => {
    expect(validateIC('980431-10-5678')).toContain('30 days'); // April 31st
  });

  it('rejects invalid days for February', () => {
    expect(validateIC('980230-10-5678')).toContain('February'); // Feb 30th
  });
});

describe('Phone Normalization (normalizeMYPhone)', () => {
  it('formats standard 01x numbers to +60', () => {
    expect(normalizeMYPhone('0123456789')).toEqual({ value: '+60123456789' });
  });

  it('handles spaces and hyphens cleanly', () => {
    expect(normalizeMYPhone('012-345 6789')).toEqual({ value: '+60123456789' });
  });

  it('accepts numbers already using +60 or 60 prefix', () => {
    expect(normalizeMYPhone('+60123456789')).toEqual({ value: '+60123456789' });
    expect(normalizeMYPhone('60123456789')).toEqual({ value: '+60123456789' });
  });

  it('rejects phone numbers containing letters', () => {
    expect(normalizeMYPhone('012-abc-6789').error).toContain('digits');
  });

  it('validates correct length for 011 numbers (11 digits total)', () => {
    expect(normalizeMYPhone('01123456789')).toEqual({ value: '+601123456789' }); // Valid length
    expect(normalizeMYPhone('0112345678').error).toContain('11 digits'); // Too short
  });

  it('validates correct length for non-011 numbers (10 digits total)', () => {
    expect(normalizeMYPhone('012345678').error).toContain('10 digits'); // Too short
  });

  it('rejects numbers that do not start with a valid mobile prefix', () => {
    expect(normalizeMYPhone('0312345678').error).toContain('starting with 01'); // Landline prefix
  });
});
