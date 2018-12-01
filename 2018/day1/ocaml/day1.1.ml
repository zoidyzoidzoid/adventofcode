open Printf

let file = Sys.argv.(1)

let () =
     let ic = open_in file in
     let freq = ref 0 in
     let rec build_list infile =
          try
               let line = input_line infile in
               line :: build_list(infile)
          with End_of_file ->
               close_in infile;
               [] in
     let rec soln = function
          [] -> print_int(!freq)
          | e::l -> freq := !freq + int_of_string(e); soln l in
     soln(build_list(ic))

