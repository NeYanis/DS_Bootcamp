import sys
from analytics import Research, Analytics
from config import num_of_steps, report_template

def main():
    if len(sys.argv) != 2:
        raise ValueError("Incorrect number of arguments is given")
    else:
            res = Research(sys.argv[1])
            data = res.file_reader()
            an = Analytics(data)

            heads, tails = an.counts()

            head_procent, tail_procent = an.fractions(heads, tails)
            random = Analytics.predict_random(num_of_steps)
            pred_heads = sum(row[0] for row in random)
            pred_tails = sum(row[1] for row in random)

            last = Analytics.predict_last(data)

            print(data)
            print(heads, tails)
            print(head_procent, tail_procent)
            print(random)
            print(last)

            report = report_template.format(
                observations = heads+tails,
                tails=tails,
                heads=heads,
                head_proc=head_procent,
                tail_proc=tail_procent,
                num_of_steps=num_of_steps,
                pred_heads = pred_heads,
                pred_tails = pred_tails
            )
            Analytics.save_file(report, "report", "txt")


if __name__ == '__main__':
    main()
