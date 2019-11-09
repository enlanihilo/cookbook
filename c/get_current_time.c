#include <stdio.h>
#include <time.h>

/*
	in this program we are exploring how to use structs by
	using the tm struct in the time.h lib.

	struct tm {
		int tm_sec;
		int tm_min;
		int tm_hour;
		int tm_mday;
		int tm_mon;
		int tm_year;
		int tm_wday;
		int tm_yday;
		int tm_isdst;
	};
*/

int main(void)
{
	long int seconds_since_epoch; // Time on unix systems is kept relative to January 1 1970.
	struct tm current_time, *time_ptr;
	int hour, minute, second, day, month, year;

	seconds_since_epoch = time(0); //pass time a null ptr as arg
	printf("time() - seconds since epoch: %ld\n", seconds_since_epoch);

	time_ptr = &current_time;

	localtime_r(&seconds_since_epoch, time_ptr);

	//3 diff ways to access struct elements
	hour   = current_time.tm_hour;	// direct access
	minute = time_ptr->tm_min;		// via pointer
	second = *((int *) time_ptr);		// hacky pointer access

	printf("Current time is: %02d:%02d:%02d\n", hour, minute, second);
}
