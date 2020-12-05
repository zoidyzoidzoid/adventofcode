defmodule Soln do

  def a do
    lines =
      File.read!("input.txt")
      |> String.split("\n")
      |> Enum.slice(0..-2)
      |> Enum.map(fn i ->
        {a, _} = Integer.parse(i)
        a
      end)
    for {x, index} <- Enum.with_index(lines) do
      for y <- Enum.slice(lines, index..-1) do
        case x + y do
          2020 ->
            IO.puts(x * y)
          _ ->
            nil
        end
      end
    end
  end

  def b do
    lines =
      File.read!("input.txt")
      |> String.split("\n")
      |> Enum.slice(0..-2)
      |> Enum.map(fn i ->
        {a, _} = Integer.parse(i)
        a
      end)
    for {x, index} <- Enum.with_index(lines) do
      for {y, index2} <- Enum.with_index(Enum.slice(lines, index..-1)) do
        for z <- Enum.slice(lines, index2..-1) do
          case x + y + z do
            2020 ->
              IO.puts(x * y * z)
            _ ->
              nil
          end
        end
      end
    end
  end
end

Soln.a()
Soln.b()
