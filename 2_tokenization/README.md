# Tokenization/Preprocessing
- Estimated time: 1 hour

The data is still in text format while Megatron expects pretokenized data. Thus, the preprocessing extracts given a tokenizer the token ids for the text in this step.
To preprocess the data use the following

```bash
sbatch tokenization.job
```

The output is an index file (idx) and the binary (bin) of the tokenizer model.

As before, don't forget to edit the job file with the path of your project space:

```bash
export PROJECT_SPACE=/projects/0/prjsXXXX
```