import { formatPrice } from '../utils/formatters.js';

/**
 * ReportGenerator for financial reports
 * Depends on formatPrice utility
 */
export class ReportGenerator {
  constructor(data) {
    this.data = data;
  }

  generateSalesReport() {
    const totalSales = this.data.reduce((sum, sale) => sum + sale.amount, 0);
    
    return {
      period: this.data.period,
      totalSales: formatPrice(totalSales),
      averageSale: formatPrice(totalSales / this.data.length),
      transactions: this.data.length
    };
  }

  generateRevenueBreakdown() {
    const breakdown = {};
    
    this.data.forEach(sale => {
      const category = sale.category;
      if (!breakdown[category]) {
        breakdown[category] = 0;
      }
      breakdown[category] += sale.amount;
    });

    // Format all values
    Object.keys(breakdown).forEach(key => {
      breakdown[key] = formatPrice(breakdown[key]);
    });

    return breakdown;
  }
}
