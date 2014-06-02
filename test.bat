@echo off
java -Xms1000m -Xmx6000m -jar D:\Development\RankLib\bin\RankLib.jar -load data/LambdaMART_20_fold/model_all_quartile_new.txt -rank data/test_set_VU_DM_2014_ranklib.txt -score data/LambdaMART_20_fold/scorefile_num_quartile_new.txt 
pause
