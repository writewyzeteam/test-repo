import { formatPrice } from '../utils/formatters.js';

/**
 * ProductCard component displays product information
 * Depends on formatPrice utility
 */
export class ProductCard {
  constructor(product) {
    this.product = product;
  }

  render() {
    const priceDisplay = formatPrice(this.product.price, this.product.currency);
    
    return `
      <div class="product-card">
        <h3>${this.product.name}</h3>
        <p class="price">${priceDisplay}</p>
        <p class="description">${this.product.description}</p>
      </div>
    `;
  }

  getDisplayPrice() {
    return formatPrice(this.product.price, this.product.currency);
  }
}
