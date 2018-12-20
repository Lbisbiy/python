class GetURL:
    def __init__(self):
        pass

    @staticmethod
    def get_base_url(*args):
        url = ""
        try:
            url = "https://{}{}{}{}?".format(*args)

        except Exception as exc:
            print("ERROR: {}".format(exc))

        return url


