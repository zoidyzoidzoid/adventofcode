let part_two ?file_name:(file=Sys.argv.(1)) () =
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
     let intermediate = ref 0.0 in
     let rec soln = function
          [] ->
                print_float(floor(!result))
          | e::l ->
                intermediate := calc(float_of_string(e));
                while !intermediate >= 0.0 do
                        result := !result +. !intermediate;
                        intermediate := calc(!intermediate);
                done;
                soln l in
     soln(build_list(ic));
     !result

let () =
        let _ = part_two() in
                ()
