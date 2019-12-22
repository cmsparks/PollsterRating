import pandas as pd
import generate_results.poll_formatter as pf

def main():
    polls = pf.3wk_as_dataframe()
    polls.to_csv("../out/empty_polls.csv")

if  __name__ =='__main__':
    main()
