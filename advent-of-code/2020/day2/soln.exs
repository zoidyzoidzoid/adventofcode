defmodule Soln do

  def a do
    File.read!("input.txt")
    |> String.split("\n")
    |> Enum.slice(0..-2)
    |> Enum.reduce(
      0,
      fn i, acc ->
        [a, b, c, d] = String.split(i, ["-", " ", ": "])
        count = Enum.count(String.codepoints(d), &(&1 == c))
        {a, _} = Integer.parse(a)
        {b, _} = Integer.parse(b)
        case count do
          x when x >= a and x <= b ->
            acc + 1
          _ ->
            acc
        end
      end)
    |> IO.puts()
  end

  def b do
    File.read!("input.txt")
    |> String.split("\n")
    |> Enum.slice(0..-2)
    |> Enum.reduce(
      0,
      fn i, acc ->
        [a, b, c, d] = String.split(i, ["-", " ", ": "])
        {a, _} = Integer.parse(a)
        {b, _} = Integer.parse(b)
        {a, b} = {a - 1, b - 1}
        d = String.codepoints(d)
        l = Enum.at(d, a)
        r = Enum.at(d, b)
        cond do
          (l == c and r != c) or (l != c and r == c) ->
            acc + 1
          true ->
            acc
        end
      end)
    |> IO.puts()
  end
end

Soln.a()
Soln.b()
