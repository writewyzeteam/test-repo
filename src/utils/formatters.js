/**
 * Shared utility functions for data formatting
 * Used across multiple modules in the application
 */

/**
 * Formats a price value with currency symbol
 * @param {number} amount - The price amount
 * @param {string} currency - Currency code (USD, EUR, GBP)
 * @returns {string} Formatted price string
 */
export function formatPrice(amount, currency = 'USD') {
  const symbols = {
    'USD': '$',
    'EUR': '€',
    'GBP': '£'
  };
  
  return `${symbols[currency]}${amount.toFixed(2)}`;
}

/**
 * Formats a date string to readable format
 * @param {string} dateString - ISO date string
 * @returns {string} Formatted date
 */
export function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });
}

/**
 * Validates email format
 * @param {string} email - Email address to validate
 * @returns {boolean} True if valid email
 */
export function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}
