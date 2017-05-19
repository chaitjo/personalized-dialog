from sys import argv
import argparse


def parse_dialogs(filename, with_history, ignore_options):
    dialogs = []
    with open(filename, 'r') as f:
        dialog = []
        for line in f:
            if line.strip() == '':
                dialogs.append(dialog)
                dialog = []
            else:
                splitted = line.strip().split('\t')
                if len(splitted) == 1 and ignore_options:
                    continue
                elif len(splitted) == 1:
                    raise ValueError('Line has not 2 utterances (seems like an option) {}'.format(splitted))
                user_utt, bot_utt = splitted
                utt_num = user_utt.split(' ')[0]
                user_utt = ' '.join(user_utt.split(' ')[1:])
                if user_utt == '':
                    user_utt = '<SILENCE>'

                if bot_utt == '':
                    bot_utt = '<SILENCE>'
                if with_history:
                    if len(dialog) > 0:
                        prev_step = dialog[len(dialog) - 1]
                        user_utt_with_history = "{} {} {}".format(prev_step[1], prev_step[2], user_utt)
                    else:
                        user_utt_with_history = user_utt
                    dialog.append((utt_num, user_utt_with_history, bot_utt))
                else:
                    dialog.append((utt_num, user_utt, bot_utt))
    return dialogs


def _parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--input', help='Path to filename')
    parser.add_argument('--with_history', action='store_true', default=False)
    parser.add_argument('--ignore_options', action='store_true', default=False)

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = _parse_args()
    dialogs = parse_dialogs(args.input, args.with_history, args.ignore_options)
    for dialog in dialogs:
        for _, user_utt, bot_utt in dialog:
            print('{}\t{}'.format(user_utt, bot_utt))
