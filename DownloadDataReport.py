import os
import logging
from report_api import case_IrnDocDetails
LOGGER = logging.getLogger('report_api')
LOGGER.setLevel(logging.INFO)

def main():
    report_type = os.environ.get("ReportName","")
    if report_type == "IRN Doc Details":
        case_IrnDocDetails()
    else:
        LOGGER.info("Report Name not found.")
        
if __name__=="__main__":
    main()
    