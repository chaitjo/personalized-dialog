if which gshuf >/dev/null; then
  shuf_cmd="gshuf"
else
  shuf_cmd="shuf"
fi

function parse_dialogs {
  prefix=$1
  task=$2
  additional_options="$3"
  base_path=../data/modified-tasks
  python parse_dialogs.py --input $base_path/$prefix-trn.txt $additional_options > data/train-$task.tsv
  python parse_dialogs.py --input $base_path/$prefix-dev.txt $additional_options > data/dev-$task.tsv
  python parse_dialogs.py --input $base_path/$prefix-tst.txt $additional_options > data/test-$task.tsv
  eval $shuf_cmd -n 500 data/dev-$task.tsv > data/dev-$task-500.tsv
  cat data/train-$task.tsv data/dev-$task.tsv data/test-$task.tsv | python build_vocabulary.py > data/vocab-$task.tsv
}
