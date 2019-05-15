from django.shortcuts import render,redirect
import datetime
from django.utils import timezone
from .models import Coupon
from .forms import CouponApplyForm
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
# from django.views.decorators.http import require_GET, require_POST
# @require_POST
def coupon_apply(request):
	registed = False
	now=timezone.now()
	form = CouponApplyForm(request.POST)
	if form.is_valid():
		code=form.cleaned_data['code']
		try:
			coupon = Coupon.objects.get(code_iexact=code,
				                        valid_from_lte=now,
				                        valid_to_gte=now,
				                        active=True)
			requset.session['coupon_id']=coupon.id
			registed = True
		except Coupon.DoesNotExit:
			requset.session['coupon_id']=None
	# return redirect('coupon_apply')
	return render(request,'code_number.html',{'form':form,'registed':registed})
def connect(request):
	return render(request,'connect.html')

def exist(request):
	coupon_apply_form = CouponApplyForm()
	return render(request,'code_number.html',{'coupon_apply_form':coupon_apply_form})

