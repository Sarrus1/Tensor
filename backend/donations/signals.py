from .models import Donators, Tvip
from dateutil.relativedelta import relativedelta
from django.utils import timezone
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from django.dispatch import receiver
import logging
log = logging.getLogger(__name__)


@receiver(valid_ipn_received)
def PaypalValidIPN(sender, **kwargs):
    log.error('valid_received')
    ipn_obj = sender
    if ipn_obj.payment_status == "Completed":
        SteamID = str(ipn_obj.option_selection1)
        SteamID_crop = SteamID[8:]
        amount = int(ipn_obj.mc_gross)
        Name = str(ipn_obj.option_selection2)
        today = timezone.now()

        myresult = Tvip.objects.filter(
            playerid=SteamID_crop, enddate__gte=today)
        if len(myresult) == 0:
            if int(amount) >= 15:
                end = today + relativedelta(years=+1)
            elif int(amount) >= 5:
                end = today + relativedelta(months=+3)
            elif int(amount) >= 2:
                end = today + relativedelta(months=+1)
            elif int(amount) >= 1:
                end = today + relativedelta(weeks=+1)
            end = end.strftime('%Y-%m-%d %H:%M:%S')
            newVip = Tvip(playername=Name,
                          playerid=SteamID_crop,
                          enddate=end,
                          admin_playername="SERVER-CONSOLE",
                          admin_playerid="SERVER-CONSOLE")
            newVip.save()
        else:
            oldVip = myresult.first()
            old_end = oldVip.enddate
            if old_end < today:
                old_end = today
            if int(amount) >= 15:
                end = old_end + relativedelta(years=+1)
            elif int(amount) >= 5:
                end = old_end + relativedelta(months=+3)
            elif int(amount) >= 2:
                end = old_end + relativedelta(months=+1)
            elif int(amount) >= 1:
                end = old_end + relativedelta(weeks=+1)
            oldVip.enddate = end
            oldVip.save()
        Donators(SteamID=SteamID, amount=amount, Name=Name, date=today).save()


@receiver(invalid_ipn_received)
def PaypalInvalidIPN(sender, **kwargs):
    log.error('invalid_received')
