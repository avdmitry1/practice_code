TAX_RATE = 0.05
class ServiceQuote:
    def __init__(self, pcharge, lcharge):
        self._parts_charges = pcharge
        self._labor_charges = lcharge
        
    def set_parts_charges(self, pcharge):
        self._parts_charges = pcharge

    def set_labor_charges(self, lcharge):
        self._labor_charges = lcharge
        
    def get_parts_charges(self):
        return self._parts_charges
    
    def get_labor_charges(self):
        return self._labor_charges
    
    def get_sales_tax(self):
        return self._parts_charges * TAX_RATE
    
    def get_total_charges(self):
        return self._parts_charges + self._labor_charges + (self._parts_charges * TAX_RATE)