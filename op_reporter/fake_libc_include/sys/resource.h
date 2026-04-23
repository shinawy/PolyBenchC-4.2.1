struct rusage {
  long ru_utime;
  long ru_stime;
};
int getrusage(int who, struct rusage *usage);
