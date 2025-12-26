from report_summarization.crew import ReportSummarization 

def run():
    """It runs the report summarization"""
    #Define the inputs
    inputs = {"field": "Education"}

    #Create the crew 
    my_crew = ReportSummarization().crew()

    #Pass the inputs to crew and execute the crew 
    result = my_crew.kickoff(inputs= inputs)

if __name__ == "__main__":
    run()

    