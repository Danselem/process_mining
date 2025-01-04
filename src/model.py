import pm4py

if __name__ == "__main__":
    log = pm4py.read_xes('./data/running-example.xes')

    dfg, start_activities, end_activities = pm4py.discover_dfg(log)

    map = pm4py.discover_heuristics_net(log)

    process_tree = pm4py.discover_process_tree_inductive(log)
    bpmn_model = pm4py.convert_to_bpmn(process_tree)
    pm4py.view_bpmn(bpmn_model)
    pm4py.view_process_tree(process_tree)
    
    pm4py.view_dfg(dfg, start_activities, end_activities)
    
    pm4py.view_heuristics_net(map)