program GCD;

const v1 = 324; v2 = 42;

var res: integer;

function GCD (m: integer; n: integer): integer;

begin
   if n = 0 then
      GCD := m
   else
      GCD := GCD(n, m mod n)
end; { GCD }

begin
   res := GCD(v1,v2);
   write('GCD(', v1, ',', v2, ') = ', res, eol);
end.
