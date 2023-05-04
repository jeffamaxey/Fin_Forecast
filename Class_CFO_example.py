import pandas as pd
import Class_Corp_Model as Corpclass


class cfo():
    def __init__(self, date_start, freq, date_end, scen, actual_estimate):
        self._date_start = date_start
        self._freq = freq
        self._date_end = date_end
        self._scenario = scen
        self._actual_estimate = actual_estimate
        self._dates = None
        self._proj_t = None

#       adding objects 
        self._fib_dict = {}
        self.fin_proj = {}

    def load_date_start(self, date_start):
        self._date_start = date_start

    @property
    def get_date_start(self):
        return self._date_start

    def load_date_end(self, date_end):
        self._date_end = date_end

  
    @property
    def get_date_end(self):
        return self._date_end

    def load_freq(self, freq):
        self._freq = freq

    @property
    def get_freq(self):
        return self._freq
#dates
    def load_scenario(self, scenario):
        self._scenario = scenario

    @property
    def get_scenario(self):
        return self._scenario

    '''
    B 	business day frequency
    C 	custom business day frequency
    D 	calendar day frequency
    W 	weekly frequency
    M 	month end frequency
    SM 	semi-month end frequency (15th and end of month)
    BM 	business month end frequency
    CBM 	custom business month end frequency
    MS 	month start frequency
    SMS 	semi-month start frequency (1st and 15th)
    BMS 	business month start frequency
    CBMS 	custom business month start frequency
    Q 	quarter end frequency
    BQ 	business quarter end frequency
    QS 	quarter start frequency
    BQS 	business quarter start frequency
    A, Y 	year end frequency
    BA, BY 	business year end frequency
    AS, YS 	year start frequency
    BAS, BYS 	business year start frequency
    BH 	business hour frequency
    H 	hourly frequency
    T, min 	minutely frequency
    S 	secondly frequency
    L, ms 	milliseconds
    U, us 	microseconds
    N 	nanoseconds
    '''
    def load_dates(self):
        dates = list(pd.date_range(start=self._date_start, end=self._date_end, freq=self._freq))
        self._proj_t = len(dates)
        self._dates = [dates[i].date() for i in range(self._proj_t)]

    def Init_Fin_Proj(self):        
        for t in range(0, self._proj_t, 1):
            self.fin_proj[t] = {'date' : self._dates[t],'EBS_Proj': Corpclass.EBS_Dashboard(self._dates[t], self._actual_estimate, self._date_start), 'Econ_Scen' : {} }

    @property
    def get_dates(self):
        return self._dates

    def fib(self, n):
        if n in self._fib_dict:
            return self._fib_dict[n]
        if n <= 1:
            ret = 0
        elif n == 2:
            ret = 1
        else:
            ret = self.fib(n - 1) + self.fib(n - 2)
        self._fib_dict[n] = ret
        return ret

    def calc_fib_dates(self):
        self._date_dict = {}

        for n, d in enumerate(self._dates, start=1):
            self._date_dict[d] = self.fib(n)
        return pd.DataFrame.from_dict(
            self._date_dict, columns=['fib#'], orient='index'
        )
