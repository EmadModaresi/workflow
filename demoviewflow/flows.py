from viewflow import flow
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from viewflow import frontend
from .models import Shoping


@frontend.register
class ShopingFlow(Flow):
    process_class = Shoping
    start = (
        flow.Start(CreateProcessView, fields=["text",]).Permission(auto_create=True).Next(this.approve)
    )

    approve = (
        flow.View(UpdateProcessView, fields=['approved']).Permission(auto_create=True).Next(this.check_approve)
    )

    check_approve = (
        flow.If(lambda activation: activation.process.approved).Then(this.send).Else(this.end)
    )

    send = (
        flow.Handler(this.send_a_factor).Next(this.end)
    )
    end = flow.End()

    def send_a_factor(self):
        count = 0
        for shop in Shoping.objects.all():
            count += shop.foods.price
        print(count)
        return count
