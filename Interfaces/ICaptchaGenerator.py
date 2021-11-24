from abc import ABCMeta, abstractmethod


class ICaptchaGenerator(object):
    """Generates captcha image and answer for this captcha"""

    @abstractmethod
    def generate(self):
        """Creates captcha image and answer for this captcha"""
