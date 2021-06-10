

class ResetController:

    def store(self, request):
        if request.method != 'POST':
            raise Exception('method no allowed')