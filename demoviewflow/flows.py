from viewflow import flow, activation
from viewflow.base import this, Flow
# from viewflow import activation
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from viewflow import frontend
from .models import Shoping
def send_a_factor(self):
    count = 12500000
    print(count)
    return count


number = 0


def number_of_count():
    global number
    number += 1
    return number


@frontend.register
class ShopingFlow(Flow):
    process_class = Shoping
    start = (
        flow.Start(CreateProcessView, fields=["shop_name", "buier_name", "counter"]).Permission(auto_create=True).Next(
            this.approve)
    )

    approve = (
        flow.View(UpdateProcessView, fields=['approved', 'shop_name', 'buier_name', ]).Permission(
            auto_create=True).Next(this.check_approve)
    )

    check_approve = (
        flow.If(lambda activation: (activation.process.counter == number_of_count())).Then(this.send).Else(
            this.approve)
    )
    send = (
        flow.Handler(send_a_factor).Next(this.end)
    )
    end = flow.End()
