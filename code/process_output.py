#edit to replace with directory that includes results JSON files
results_dir = "../results/"


import pandas as pd
import os

full_df = pd.DataFrame(columns=["ModelName","ModelRevision","Task","Accuracy","Accuracy_SE"])

for file in os.listdir(results_dir):
    path = results_dir+file
    current_model_results = pd.read_json(path,typ="series")
    split_model_args = current_model_results["config"]["model_args"].split(",")
    current_model_revision=None
    for arg in split_model_args:
        if "pretrained=" in arg:
            current_model_name = arg.split("=")[1]
        if "revision=" in arg:
            current_model_revision = arg.split("=")[1]
    all_results = current_model_results["results"]
    for task in all_results:
        task_name=task
        if task!="truthfulqa_mc":
            acc,acc_stderr=None,None
            for eval_metric in all_results[task]:
                if eval_metric=="acc":
                    acc= all_results[task][eval_metric]
                if eval_metric=="acc_stderr":
                    acc_stderr = all_results[task][eval_metric]
            current_task_results = pd.DataFrame({"ModelName":[current_model_name],
                                                 "ModelRevision":[current_model_revision],
                                                 "Task":[task_name],
                                                 "Accuracy":[acc],
                                                 "Accuracy_SE":[acc_stderr]})
            full_df = pd.concat([full_df,current_task_results]).reset_index(drop=True)
        else:
            mc1_acc,mc1_stderr,mc2_acc,mc2_stderr=None,None,None,None
            for eval_metric in all_results[task]:
                if eval_metric=="mc1":
                    mc1_acc = all_results[task][eval_metric]    
                if eval_metric=="mc1_stderr":
                    mc1_stderr = all_results[task][eval_metric]    
                if eval_metric=="mc2":
                    mc2_acc = all_results[task][eval_metric]    
                if eval_metric=="mc2_stderr":
                    mc2_stderr = all_results[task][eval_metric]    
            current_task_results = pd.DataFrame({"ModelName":[current_model_name],
                                                 "ModelRevision":[current_model_revision],
                                                 "Task":[task_name+"1"],
                                                 "Accuracy":[mc1_acc],
                                                 "Accuracy_SE":[mc1_stderr]})
            full_df = pd.concat([full_df,current_task_results]).reset_index(drop=True)                
            current_task_results = pd.DataFrame({"ModelName":[current_model_name],
                                                 "ModelRevision":[current_model_revision],
                                                 "Task":[task_name+"2"],
                                                 "Accuracy":[mc2_acc],
                                                 "Accuracy_SE":[mc2_stderr]})
            full_df = pd.concat([full_df,current_task_results]).reset_index(drop=True)
            
full_df.to_csv(results_dir+"all_results.tsv",sep="\t",index=False)