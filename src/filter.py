import pm4py
import datetime as dt

if __name__ == "__main__":
    log = pm4py.read_xes('./data/running-example.xes')

    filtered = pm4py.filter_start_activities(log, {'register request'})

    filtered = pm4py.filter_start_activities(log, {'register request TYPO!'})

    filtered = pm4py.filter_end_activities(log, {'pay compensation'})

    filtered = pm4py.filter_event_attribute_values(log, 'org:resource', {'Pete', 'Mike'})

    filtered = pm4py.filter_event_attribute_values(log, 'org:resource', {'Pete', 'Mike'}, level='event')

    filtered = pm4py.filter_trace_attribute_values(log, 'concept:name', {'3', '4'})

    filtered = pm4py.filter_trace_attribute_values(log, 'concept:name', {'3', '4'}, retain=False)

    filtered = pm4py.filter_variants(log, [
        ['register request', 'check ticket', 'examine casually', 'decide', 'pay compensation']])

    filtered = pm4py.filter_variants(log, [
        ['register request', 'check ticket', 'examine casually', 'decide', 'reject request']])

    filtered = pm4py.filter_directly_follows_relation(log, [('check ticket', 'examine casually')])

    filtered = pm4py.filter_eventually_follows_relation(log, [('examine casually', 'reject request')])

    filtered = pm4py.filter_time_range(log, dt.datetime(2010, 12, 30), dt.datetime(2010, 12, 31), mode='events')

    filtered = pm4py.filter_time_range(log, dt.datetime(2010, 12, 30), dt.datetime(2010, 12, 31),
                                       mode='traces_contained')

    filtered = pm4py.filter_time_range(log, dt.datetime(2010, 12, 30), dt.datetime(2010, 12, 31),
                                       mode='traces_intersecting')