// This script is run after run_fill_genus.m, and fills in additional attributes of lattices in the genus that need access to lattices in different genera.
// Usage: magma -b label:=foo run_connect_genus.m
// Batch: magma -b labels:=foo:bar:baz run_connect_genus.m
// Options: timeout:=N (default 60, seconds per label)
//
// Parallel across servers:
//   xargs -n 100 < genera_todo.txt | tr ' ' ':' > genera_todo_chunked.txt
//   parallel --sshloginfile servers.txt --joblog jobs.log --eta --resume \
//     'cd ~/projects/k3s-lmfdb/lattices && magma -b labels:={} verbose:=0 run_connect_genus.m' \
//     :::: genera_todo_chunked.txt > output.txt
//
// Errors are prefixed with "ERROR: label: ..."
// Extract retry list: grep '^ERROR:' output.txt | cut -d: -f2 | tr -d ' ' > genera_failed.txt

AttachSpec("lattices.spec");

if not assigned verbose then verbose := "0"; end if;
SetVerbose("ConnectGenus", StringToInteger(verbose));

if not assigned timeout then timeout := "60"; end if;
timeout := StringToInteger(timeout);

if assigned labels then
    label_list := Split(labels, ":");
else
    label_list := [label];
end if;

procedure() // forcing magma to read the full input before forking
failed := [];
for l in label_list do
    try
        ConnectGenus(l : timeout := timeout);
    catch e
        printf "ERROR: %o: %o\n", l, e;
        Append(~failed, l);
    end try;
end for;

if #failed gt 0 then
    exit 1;
end if;
exit 0;
end procedure();
