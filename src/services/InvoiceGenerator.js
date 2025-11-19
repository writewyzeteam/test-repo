import { formatPrice, formatDate } from '../utils/formatters.js';

/**
 * InvoiceGenerator service for creating invoices
 * Depends on formatPrice and formatDate utilities
 */
export class InvoiceGenerator {
  constructor(order) {
    this.order = order;
  }

  generateInvoice() {
    const items = this.order.items.map(item => ({
      name: item.name,
      quantity: item.quantity,
      price: formatPrice(item.price, item.currency),
      total: formatPrice(item.price * item.quantity, item.currency)
    }));

    return {
      invoiceNumber: this.order.id,
      date: formatDate(this.order.date),
      items: items,
      total: formatPrice(this.order.total, this.order.currency)
    };
  }

  exportToPDF() {
    const invoice = this.generateInvoice();
    // PDF export logic would go here
    return invoice;
  }
}
