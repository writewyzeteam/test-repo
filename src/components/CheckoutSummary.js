import { formatPrice } from '../utils/formatters.js';

/**
 * CheckoutSummary component for order totals
 * Depends on formatPrice utility
 */
export class CheckoutSummary {
  constructor(items) {
    this.items = items;
  }

  calculateTotal() {
    return this.items.reduce((sum, item) => sum + item.price, 0);
  }

  render() {
    const subtotal = this.calculateTotal();
    const tax = subtotal * 0.08;
    const total = subtotal + tax;

    return `
      <div class="checkout-summary">
        <div class="line-item">
          <span>Subtotal:</span>
          <span>${formatPrice(subtotal)}</span>
        </div>
        <div class="line-item">
          <span>Tax:</span>
          <span>${formatPrice(tax)}</span>
        </div>
        <div class="line-item total">
          <span>Total:</span>
          <span>${formatPrice(total)}</span>
        </div>
      </div>
    `;
  }
}
