@echo off
java -Xms1000m -Xmx6000m -jar D:\Development\RankLib\bin\RankLib.jar -load data/LambdaMART_20_fold/model_all.txt -rank data/test_ranklib.txt -score data/LambdaMART_20_fold/scorefile_all.txt 
pause
