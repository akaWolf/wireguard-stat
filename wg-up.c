#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
    setuid( 0 );   // you can set it at run time also
    system( "wg-quick up wg0" );
    return 0;
}
