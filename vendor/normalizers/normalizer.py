class MobileNormalizer:
    def normalize_mobile(self, mobile):
        if mobile is None:
            return None
        d = {'۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4', '۵': '5', '۶': '6',
             '۷': '7', '۸': '8', '۹': '9'}

        for char in mobile:
            if char in d:
                mobile = mobile.replace(char, d[char])

        return mobile
