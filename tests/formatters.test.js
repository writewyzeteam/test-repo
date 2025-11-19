import { formatPrice, formatDate, validateEmail } from '../src/utils/formatters.js';

describe('Formatters Utility Tests', () => {
  describe('formatPrice', () => {
    test('formats USD correctly', () => {
      expect(formatPrice(29.99, 'USD')).toBe('$29.99');
    });

    test('formats EUR correctly', () => {
      expect(formatPrice(29.99, 'EUR')).toBe('€29.99');
    });

    test('formats GBP correctly', () => {
      expect(formatPrice(29.99, 'GBP')).toBe('£29.99');
    });

    test('defaults to USD', () => {
      expect(formatPrice(29.99)).toBe('$29.99');
    });

    test('rounds to 2 decimal places', () => {
      expect(formatPrice(29.999, 'USD')).toBe('$30.00');
    });
  });

  describe('formatDate', () => {
    test('formats ISO date correctly', () => {
      expect(formatDate('2024-01-15')).toContain('January');
      expect(formatDate('2024-01-15')).toContain('15');
      expect(formatDate('2024-01-15')).toContain('2024');
    });
  });

  describe('validateEmail', () => {
    test('validates correct email', () => {
      expect(validateEmail('test@example.com')).toBe(true);
    });

    test('rejects invalid email', () => {
      expect(validateEmail('invalid.email')).toBe(false);
    });
  });
});
