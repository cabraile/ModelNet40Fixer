DS_PATH="/path/to/dataset";
FIXER_PATH="/absolute/path/to/fixer";

fix_class()
{
  S_CLASS=$1;
  cd ${S_CLASS};
  for INSTANCE in `ls train/*.off`; do
    python ${FIXER_PATH}/fixer.py ${INSTANCE}
  done
  for INSTANCE in `ls test/*.off`; do
    python ${FIXER_PATH}/fixer.py ${INSTANCE}
  done
  cd .. ;
}

cd $DS_PATH;
for S_CLASS in `ls -d */` ; do
  fix_class ${S_CLASS} &
done
