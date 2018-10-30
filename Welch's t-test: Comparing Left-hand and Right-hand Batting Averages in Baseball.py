import numpy
import scipy.stats
import pandas

def compare_averages(filename):
    """
    Performs a t-test on two sets of baseball data (left-handed and right-handed hitters).

    You will be given a csv file that has three columns.  A player's
    name, handedness (L for lefthanded or R for righthanded) and their
    career batting average (called 'avg'). You can look at the csv
    file by downloading the baseball_stats file from Downloadables below. 
    
    Write a function that will read that the csv file into a pandas data frame,
    and run Welch's t-test on the two cohorts defined by handedness.
    
    One cohort should be a data frame of right-handed batters. And the other
    cohort should be a data frame of left-handed batters.
    
    We have included the scipy.stats library to help you write
    or implement Welch's t-test:
    http://docs.scipy.org/doc/scipy/reference/stats.html
    
    With a significance level of 95%, if there is no difference
    between the two cohorts, return a tuple consisting of
    True, and then the tuple returned by scipy.stats.ttest.  
    
    If there is a difference, return a tuple consisting of
    False, and then the tuple returned by scipy.stats.ttest.
    
    For example, the tuple that you return may look like:
    (True, (9.93570222, 0.000023))
    """
    df = pandas.read_csv(filename)
    df = df[["name","handedness","avg"]]
  
    #because count() does not count NaN-s
    #print(df["handedness"].count())

    df["handedness"] = df["handedness"].replace("", numpy.NaN)
    df.dropna(axis = 0, subset=["handedness"],inplace=True)

    rightH = []
    leftH = []
    for i, row in df.iterrows():

     dict1 = {} 
     if row["handedness"]=="R":
             dict1 = row
             rightH.append(dict1)
     if row["handedness"]=="L":
             dict1=row
             leftH.append(dict1)
    rightH = pandas.DataFrame(data = rightH,columns = ["avg"])
    leftH = pandas.DataFrame(data = leftH, columns = ["avg"])     
      
    print(rightH.head())
    t_val, p_val = scipy.stats.ttest_ind( rightH, leftH, equal_var=False)
    if p_val<0.05:
        #If p is less than P-critical, then
        #our test is Insignificant
        #Null hypothesis is False, we reject it,
        #which means there IS a difference between 2 groups.
        return (False, (t_val, p_val))
    return (true, (t_val, p_val)) 
