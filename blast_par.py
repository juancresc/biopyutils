from subprocess import Popen, PIPE, call
import Queue
from threading import Thread, Lock, active_count
import os
def blast(q):
    while True:
        count, query = q.get()
        subject_filename = 'tmp/' + str(count) + '.fasta'
        out_filename = 'tmp/res_' + str(count) + '.csv'
        cmd_list = [
        'blastn',
        '-query', query,
        '-task', 'blastn',
        '-qcov_hsp_perc', '90',
        '-evalue', '10e-3',
        '-subject', subject_filename,
        '-outfmt', '6']
        pro = Popen(cmd_list, stdout=PIPE, stderr=PIPE)
        out,err = pro.communicate()
        if err:
            print(err)
            q.task_done()
        out_file = open(out_filename, 'w')
        out_file.write(out)
        out_file.close()
        os.remove(subject_filename)
        q.task_done()

def blast_par(query, subject, params, output, threads):
    import os
    from Bio import SeqIO

    if not os.path.isdir('tmp/'):
        os.mkdir('tmp/')
    #separate subject in files
    count = 0
    fasta_seq = SeqIO.parse(subject, 'fasta')
    for record in fasta_seq:
        count += 1
        subject_filename = 'tmp/' + str(count) + '.fasta'
        SeqIO.write(record, subject_filename , 'fasta')
    
    #create workers
    queue = Queue.Queue(maxsize=0)
    workers = []
    for i in range(threads):
        worker = Thread(target=blast, args=(queue,))
        worker.setDaemon(True)
        worker.start()
        workers.append(worker)


    #send tasks workers
    for i in range(1,count + 1):
        queue.put((i, query))

    #wait for finalization
    queue.join()

    #merge results
    output_file = open(output,'w')
    for res_file in os.listdir('tmp/'):
        filename = 'tmp/' + res_file
        if not res_file.startswith('res_'):
            print(res_file)
            continue
        res = open(filename, 'r')
        lines = res.readlines()
        for line in lines:
            output_file.write(line)
        res.close()
        os.remove(filename)
    output_file.close()
    
    print('done')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()#pylint: disable=invalid-name
    parser.add_argument('-t', '--threads', help='Number of threads to use, default 1', default=1, type=int)
    parser.add_argument('-q', '--query', help='BLAST query', required=True)
    parser.add_argument('-s', '--subject', help='BLAST subject', required=True)
    parser.add_argument('-p', '--params', help='additional BLAST parameters (between quotes')
    parser.add_argument('-o', '--output', help='Output file in .fasta format', required=True)
    args = parser.parse_args()#pylint: disable=invalid-name
    blast_par(args.query, args.subject, args.params, args.output, args.threads)
