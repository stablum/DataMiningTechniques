@echo off
set @stime=%time%
java -Xms1000m -Xmx6000m -jar D:\Development\RankLib\bin\RankLib.jar -train data/training_set_VU_DM_2014_ranklib.txt -ranker 6 -metric2t NDCG@38 -save data\LambdaMART_20_fold\model_all_new.txt -norm linear
set @etime=%time%
echo %@stime%
echo %@etime%
pause
