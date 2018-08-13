
      subroutine gridloop2(a, xcoor, ycoor, nx, ny)
      integer nx, ny
      real*8 a(nx,ny), xcoor(nx), ycoor(ny)
Cf2py intent(out) a
Cf2py depend(nx,ny) a

      integer i,j
      real*8 x, y
      do j = 1,ny
         y = ycoor(j)
         do i = 1,nx
            x = xcoor(i)
            a(i,j) = sin(x*y) + 8*x
         end do
      end do
      return
      end
