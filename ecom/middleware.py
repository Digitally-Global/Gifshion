def simplemiddleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        try:
            print(request.session["currency_code"])
        except:
            request.session['currency_code'] = 'INR'
            request.session['exchange']=float(1.0)
            request.session["icon"]='₹'
        response = get_response(request)
        print("After response")
        return response

    return middleware
