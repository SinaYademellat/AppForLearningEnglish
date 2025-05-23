"""_summary_
 لغت های همان روز را داریم 
 لعت های دیروز
 و 
 ...

 اگر هم جایی اشتباه کریم باید بیام همان اول کار

 دیتاست ها هم به شکل پیل ذخیره می کنیم
"""

class Lernkartei_word:
    """
     این دیتااستراکچر اصلی کلمات هست  مثل کارت های لغت هست
    برای هر کدام از جعبه هاهم به شکل یک فایل درست ذخیره کردم
    """
    def __init__(self, Txt:str  ,  Collocations:str = None , Status:int=None  ) -> None:
        """_summary_

        Args:
            Txt (str): _description_
            Status (int):
                day 1  : ==> 1
                day 2  : ==> 2
                day 3  : ==> 3
                week 1 : ==> 4
                week 2 : ==> 5
                Months : ==> 6

        """
        self.txt = Txt
        self.collocations = Collocations
        self.status = Status 

    def __repr__(self):
        my_print = f"""
                Txt = {self.txt}
                col = {self.collocations}
                sta = {self.status}
            """
        
        return my_print
