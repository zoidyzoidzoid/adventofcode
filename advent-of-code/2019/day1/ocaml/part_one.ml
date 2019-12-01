let solution ?file_name:(file=Sys.argv.(1)) () =
     let ic = open_in file in
     let result = ref 0.0 in
     let calc mass = (floor(mass /. 3.0) -. 2.0) in
     let rec build_list infile =
          try
               let line = input_line infile in
               line :: build_list(infile)
          with End_of_file ->
               close_in infile;
               [] in
     let rec soln = function
          [] -> print_float(!result)
          | e::l -> result := !result +. calc(float_of_string(e)); soln l in
     soln(build_list(ic));
     !result

let () =
        let _ = solution() in
                ()
