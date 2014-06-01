@echo off
set @stime=%time%
java -Xms1000m -Xmx6000m -jar D:\Development\RankLib\bin\RankLib.jar -train data/training_set_VU_DM_2014_ranklib_all.txt -ranker 8 -metric2t NDCG@38 -save data\Random_Forests\model_all.txt -norm linear -tree 10
set @etime=%time%
echo %@stime%
echo %@etime%
pause
