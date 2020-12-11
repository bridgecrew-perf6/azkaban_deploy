es_host=""
es_port=""


# 解析所有的输入参数
while [ $# -ge 2 ]; do
  case "$1" in
    --es-host)
        es_host="$2"
        shift 2
        ;;
    --es-port)
        es_port="$2"
        shift 2
    *)
        echo "unknow parameter $1"
        exit 1
        break
        ;;
  esac
done


cd data_insight_test

path=`cd $(dirname $0);pwd -P`
echo the current path is:$path
for i in `ls`
do
        echo $i
done
filename=`basename $0`
echo file name is:$filename


python -m run_task \
  --es-host=${es_host} \
  --es-port=${es_port}
