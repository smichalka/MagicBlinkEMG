using System;
using LSL;

namespace Event_Example
{
    public delegate void MyEventHandler(object source, MyEventArgs e);

    public class MyEventArgs : EventArgs
    {
        private string EventInfo;
        public MyEventArgs(string Text)
        {
            EventInfo = Text;
        }
        public string GetInfo()
        {
            return EventInfo;
        }
    }
    public class MyClass
    {
        public event MyEventHandler OnMaximum;
        private double i;
        private int Maximum = 10;
        public double MyValue
        {
            get
            {
                return i;
            }
            set
            {
                if(value <= Maximum)
                {
                    i = value;
                }
                else
                {
                    if(OnMaximum != null)
                    {
                        OnMaximum(this, new MyEventArgs("You've entered " + value.ToString() + ", but the maximum is " + Maximum.ToString()));
                    }
                }
            }
        }
    }

    class Program
    {
        static void MaximumReached(object source, MyEventArgs e)
        {
            Console.WriteLine(e.GetInfo());
        }
        static void Main(string[] args)
        {
            MyClass MyObject = new MyClass();
            MyObject.OnMaximum += new MyEventHandler(MaximumReached);
            StreamInfo[] results = LSL.LSL.resolve_stream("name", "MyMarkerStream", 1, 0.5f);
            StreamInlet inlet = new StreamInlet(results[0]);
            string[] sample = new string[1];
            for(int x = 0; x<=15; x++)
            {
                MyObject.MyValue = inlet.pull_sample(sample);
            }

            Console.ReadLine();
        }
    }
}