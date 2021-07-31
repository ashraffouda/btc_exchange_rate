from django.db import models

# A model for BTC/USD exchange rate
class ExchangeEntry(models.Model):
    rate = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.rate} USD - {str(self.time)}"