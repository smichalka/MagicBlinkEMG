using System;

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
        private int i;
        private int Maximum = 10;
        public int MyValue
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

            for(int x = 0; x<=150; x++)
            {
                MyObject.MyValue = x;
                Console.WriteLine(x.ToString());
            }

            Console.ReadLine();
        }
    }
}