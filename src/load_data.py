import pandas as pd
import pm4py


def import_csv(file_path):
    event_log = pd.read_csv(file_path, sep=';')
    num_events = len(event_log)
    num_cases = len(event_log.case_id.unique())
    print("Number of events: {}\nNumber of cases: {}".format(num_events, num_cases))

    event_log = pm4py.format_dataframe(event_log, case_id='case_id',
    activity_key='activity', timestamp_key='timestamp')
    event_log.to_csv('./data/running-example-exported.csv')
    pm4py.write_xes(event_log, './data/running-example-exported.xes')


if __name__ == "__main__":
    import_csv("./data/running-example.csv")